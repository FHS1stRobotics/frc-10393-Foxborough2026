import robotpy_apriltag as at
from robotpy_apriltag import AprilTagPoseEstimator
import cv2 as cv # opencv-python (needs install on roborio)
from collections.abc import Buffer
import constants as const
import threading
# 0.158

class AprilTag:
    def __init__(self) -> None:
        self.detector = at.AprilTagDetector()
        # self.pose_estimator = AprilTagPoseEstimator(
        #     AprilTagPoseEstimator.Config(
        #         tagSize=0.158, # meters
        #         fx=fx,
        #         fy=fy,
        #         cx=cx,
        #         cy=cy
        #     )
        # )
    
    def test_apriltag_detection(self):
        detections = self.detector.detect(self.get_webcam_buffer())
        for detection in detections:
            print(detection.getCenter())
            print(detection.getCorner(0))
            print(detection.getDecisionMargin())
            print(detection.getFamily)
            print(detection.getHomography())
            print(detection.getHamming())
            print(detection.getId())
            print("\n")
    
    def parse_detections(self, detections: list[at.AprilTagDetection]):
        pass
    
    def detect(self) -> list[at.AprilTagDetection]:
        # execute in the autonomousPeriodic loop?
        return self.detector.detect(self.get_webcam_buffer())
    
    @staticmethod
    def get_webcam_buffer() -> Buffer:
        capture = cv.VideoCapture(const.kWebcamID)
        success, frame = capture.read()
        capture.release()
        
        if not success:
            raise RuntimeError("Failed to get webcam data")
        
        # converts captured frame to grayscale
        grayscaled = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
        # encode the image to png
        success, encoded = cv.imencode(".png", grayscaled)
        if not success:
            raise RuntimeError("Failed to encode image")
        
        return memoryview(encoded)
    
apriltag = AprilTag()
apriltag.test_apriltag_detection()