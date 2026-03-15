# demo.py - Fashion Angle Classifier Demo
import tensorflow as tf
import numpy as np
from PIL import Image
import argparse
import time

class FashionAngleClassifier:
    def __init__(self, model_path='final_production_model.keras'):
        print("🚀 Loading fashion angle classifier...")
        self.model = tf.keras.models.load_model(model_path)
        self.classes = ['front', 'back', 'side', 'crop', 'full', 'flat', 'infographic']
        print(f"✅ Model loaded! 7 classes: {self.classes}")
    
    def predict(self, image_path):
        # Load and preprocess image
        img = Image.open(image_path).resize((300, 300))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Predict
        start = time.time()
        predictions = self.model.predict(img_array, verbose=0)
        inference_time = time.time() - start
        
        class_idx = np.argmax(predictions[0])
        confidence = predictions[0][class_idx]
        
        return {
            'angle': self.classes[class_idx],
            'confidence': float(confidence),
            'inference_time': inference_time,
            'all_probabilities': {
                cls: float(prob) for cls, prob in zip(self.classes, predictions[0])
            }
        }
    
    def predict_batch(self, image_paths):
        results = []
        for path in image_paths:
            results.append(self.predict(path))
        return results

def main():
    parser = argparse.ArgumentParser(description='Fashion Angle Classifier')
    parser.add_argument('image', help='Path to image file')
    parser.add_argument('--model', default='final_production_model.keras', help='Model path')
    
    args = parser.parse_args()
    
    classifier = FashionAngleClassifier(args.model)
    result = classifier.predict(args.image)
    
    print(f"\n📸 Image: {args.image}")
    print(f"🎯 Predicted angle: {result['angle']}")
    print(f"📊 Confidence: {result['confidence']:.2%}")
    print(f"⏱️ Inference time: {result['inference_time']:.3f}s")
    print("\n📈 All probabilities:")
    for angle, prob in result['all_probabilities'].items():
        print(f"   {angle}: {prob:.2%}")

if __name__ == "__main__":
    main()