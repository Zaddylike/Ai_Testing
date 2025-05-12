from ultralytics import YOLO




def train_model(data_yaml: str, epochs: int = 50):
    try:
        model = YOLO('yolov5s.pt')  # 或 yolov8n.pt
        model.train(data=data_yaml, epochs=epochs, imgsz=640)
        print("[Info] 訓練完成")
    except Exception as e:
        print(f"[Error] 訓練失敗：{e}")
        raise

if __name__ == "__main__":
    train_model('data/ui_dataset.yaml', epochs=100)