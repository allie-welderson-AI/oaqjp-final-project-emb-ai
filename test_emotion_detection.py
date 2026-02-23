from EmotionDetection.emotion_detection import emotion_detector
import unittest
import json

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy
        result_1 = emotion_detector('I am glad this happened')
        result_1_dict = json.loads(result_1)
        self.assertEqual(result_1_dict["dominant_emotion"], 'joy')
        # Test case for anger
        result_2 = emotion_detector('I am really mad about this')
        result_2_dict = json.loads(result_2)
        self.assertEqual(result_2_dict["dominant_emotion"], 'anger')
        # Test case for disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        result_3_dict = json.loads(result_3)
        self.assertEqual(result_3_dict["dominant_emotion"], 'disgust')
        # Test case for sadness
        result_4 = emotion_detector('I am so sad about this')
        result_4_dict = json.loads(result_4)
        self.assertEqual(result_4_dict["dominant_emotion"], 'sadness')
        # Test case for fear
        result_5 = emotion_detector('I am really afraid that this will happen')
        result_5_dict = json.loads(result_5)
        self.assertEqual(result_5_dict["dominant_emotion"], 'fear')

unittest.main()

