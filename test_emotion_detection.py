from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(max(result_1, key=result_1.get), 'joy')

        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(max(result_2, key=result_2.get), 'anger')

        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(max(result_3, key=result_3.get), 'disgust')

        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(max(result_4, key=result_4.get), 'sadness')

        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(max(result_5, key=result_5.get), 'fear')

unittest.main()