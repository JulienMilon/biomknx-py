class KeyPoint:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


class Human3D32:
    def __init__(self, nose: KeyPoint, left_eye_inner: KeyPoint, left_eye: KeyPoint, left_eye_outer: KeyPoint,
                 right_eye_inner: KeyPoint, right_eye: KeyPoint, right_eye_outer: KeyPoint,
                 left_ear: KeyPoint, right_ear: KeyPoint,
                 mouth_left: KeyPoint, mouth_right: KeyPoint,
                 left_shoulder: KeyPoint, right_shoulder: KeyPoint,
                 left_elbow: KeyPoint, right_elbow: KeyPoint,
                 left_wrist: KeyPoint, right_wrist: KeyPoint,
                 left_pinky: KeyPoint, right_pinky: KeyPoint,
                 left_index: KeyPoint, right_index: KeyPoint,
                 left_thumb: KeyPoint, right_thumb: KeyPoint,
                 left_hip: KeyPoint, right_hip: KeyPoint,
                 left_knee: KeyPoint, right_knee: KeyPoint,
                 left_ankle: KeyPoint, right_ankle: KeyPoint,
                 left_heel: KeyPoint, right_heel: KeyPoint,
                 left_foot_index: KeyPoint, right_foot_index: KeyPoint):
        self.nose = nose
        self.left_eye_inner = left_eye_inner
        self.left_eye = left_eye
        self.left_eye_outer = left_eye_outer
        self.right_eye_inner = right_eye_inner
        self.right_eye = right_eye
        self.right_eye_outer = right_eye_outer
        self.left_ear = left_ear
        self.right_ear = right_ear
        self.mouth_left = mouth_left
        self.mouth_right = mouth_right
        self.left_shoulder = left_shoulder
        self.right_shoulder = right_shoulder
        self.left_elbow = left_elbow
        self.right_elbow = right_elbow
        self.left_wrist = left_wrist
        self.right_wrist = right_wrist
        self.left_pinky = left_pinky
        self.right_pinky = right_pinky
        self.left_index = left_index
        self.right_index = right_index
        self.left_thumb = left_thumb
        self.right_thumb = right_thumb
        self.left_hip = left_hip
        self.right_hip = right_hip
        self.left_knee = left_knee
        self.right_knee = right_knee
        self.left_ankle = left_ankle
        self.right_ankle = right_ankle
        self.left_heel = left_heel
        self.right_heel = right_heel
        self.left_foot_index = left_foot_index
        self.right_foot_index = right_foot_index

    def gravity_center(self):

        # Right Foot Center
        right_foot_center = KeyPoint(x=(self.right_foot_index.x + self.right_heel.x) / 2,
                                     y=(self.right_foot_index.y + self.right_heel.y)/2,
                                     z=(self.right_foot_index.z + self.right_heel.z)/2)

        # Left Foot Center
        left_foot_center = KeyPoint(x=(self.left_foot_index.x + self.left_heel.x) / 2,
                                    y=(self.left_foot_index.y + self.left_heel.y)/2,
                                    z=(self.left_foot_index.z + self.left_heel.z)/2)
        # Right Leg Center
        right_leg_center = KeyPoint(x=(self.right_ankle.x + self.right_knee.x)/2,
                                    y=(self.right_ankle.y + self.right_knee.y)/2,
                                    z=(self.right_ankle.z + self.right_knee.z)/2)

        # Left Leg Center
        left_leg_center = KeyPoint(x=(self.left_ankle.x + self.left_knee.x) / 2,
                                   y=(self.left_ankle.y + self.left_knee.y)/2,
                                   z=(self.left_ankle.z + self.left_knee.z)/2)

        # Right Thigh Center
        right_thigh_center = KeyPoint(x=(self.right_knee.x + self.right_hip.x) / 2,
                                      y=(self.right_knee.y + self.right_hip.y)/2,
                                      z=(self.right_knee.z + self.right_hip.z)/2)

        # Left Thigh Center
        left_thigh_center = KeyPoint(x=(self.left_knee.x + self.left_hip.x) / 2,
                                     y=(self.left_knee.y + self.left_hip.y)/2,
                                     z=(self.left_knee.z + self.left_hip.z)/2)

        # Half Bust Right to build Low Bust Center and High Bust Center
        half_bust_right = KeyPoint(x=(self.right_hip.x + self.right_shoulder.x) / 2,
                                   y=(self.right_hip.y + self.right_shoulder.y)/2,
                                   z=(self.right_hip.z + self.right_shoulder.z)/2)

        # Half Bust Left to build Low Bust Center and High Bust Center
        half_bust_left = KeyPoint(x=(self.left_hip.x + self.left_shoulder.x) / 2,
                                  y=(self.left_hip.y + self.left_shoulder.y)/2,
                                  z=(self.left_hip.z + self.left_shoulder.z)/2)

        # Low Bust Center
        low_bust_center = KeyPoint(x=(self.left_hip.x + self.right_hip.x + half_bust_left.x + half_bust_right.x)/4,
                                   y=(self.left_hip.y + self.right_hip.y + half_bust_left.y + half_bust_right.y)/4,
                                   z=(self.left_hip.z + self.right_hip.z + half_bust_left.z + half_bust_right.z)/4)

        # Low Bust Center
        high_bust_center = KeyPoint(x=(half_bust_left.x+half_bust_right.x+self.left_shoulder.x+self.right_shoulder.x)/4,
                                    y=(half_bust_left.y+half_bust_right.y+self.left_shoulder.y+self.right_shoulder.y)/4,
                                    z=(half_bust_left.z+half_bust_right.z+self.left_shoulder.z+self.right_shoulder.z)/4)


        # arms
        # forearm
        # hand
        # neck + head

        gravity_center = KeyPoint(x=0, y=0, z=0)
        return gravity_center
