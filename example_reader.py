import client


class MyModelExample:
    def preprocess_frame(self, frame):
        return frame
    
    def foward(self, inputs):
        return {
            "boxes": [[100, 100, 200, 200], [10, 50, 30, 250]], 
            "labels":[0, 2], 
            "scores":[0.95, 0.84]
            }


model = MyModelExample()


url = "rtmp://127.0.0.1:1935/live/test"

reader = client.Reader(url)


# main loop
while True:
    frame = reader.retrieve_frame()

    inputs = model.preprocess_frame(frame)
    detections = model.foward(inputs)

    print(detections)


