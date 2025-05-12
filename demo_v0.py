# infer_and_click.py
import io
from ultralytics import YOLO
from appium import webdriver

def load_model(path='runs/train/exp/weights/best.pt'):
    return YOLO(path)

def get_ui_boxes(model, screenshot_bytes):
    results = model.predict(source=screenshot_bytes, imgsz=640)
    # 取第一張圖的 bbox
    return results[0].boxes.xyxy.tolist()

def main():
    # 1. 建立 driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', {...})
    # 2. 擷取畫面
    png = driver.get_screenshot_as_png()
    # 3. 推論
    boxes = get_ui_boxes(load_model(), png)
    # 4. 點擊每個框心點
    for x1, y1, x2, y2 in boxes:
        xc, yc = int((x1+x2)/2), int((y1+y2)/2)
        try:
            driver.tap([(xc, yc)])
        except Exception as e:
            print(f"[Warn] 點擊失敗 at {(xc,yc)}: {e}")
    driver.quit()

if __name__ == "__main__":
    main()
