# Bài toán cắt thanh vật liệu
Chương trình có thể giúp người dùng đưa ra cách cắt thanh vật liệu theo yêu cầu sao cho tiết kiệm vật liệu nhất có thể. 
## Thông tin:
- **Tên**: Bài toán cắt vật liệu.
## Tính năng: 
- Đưa ra các thông số bao gồm: số lượng thanh (x)m cần cắt nhỏ nhất, tổng số thanh gốc được dùng để cắt, chiều dài thanh còn dư và phương pháp cắt.
## Hướng dẫn sử dụng:
- Bước 1: ta nhập kích thước thanh được cắt, đây sẽ là thanh vật liệu được dùng để cắt ra các thanh nhỏ hơn.
- Bước 2: ta nhập số lượng các thanh thép mà bạn cần cắt (ví dụ: bạn muốn cắt thanh vật liệu gốc thành 3 loại là 1m, 2m, 3m thì nhập là 3).
- Bước 3: lần lượt nhập chiều dài thanh mà bạn muốn cắt và số lượng thanh cần cắt.
- Ví dụ với bài toán sau: Cần cắt những thanh vật liệu có chiều dài 4m thành: 500 đoạn mà mỗi đoạn dài 1m, 300 đoạn mà mỗi đoạn dài 1,2m và 200 đoạn, mỗi đoạn dài 2,2m. Hãy thiết lập mô hình toán học cho phương án cắt vật liệu sao cho tổng độ dài của các vật liệu dư thừa là bé nhất.
- Ta lần lượt nhập: 4 3 1 500 1.2 300 2.2 200.
- Chương trình trả về số lượng (lần lượt là 2.2m, 1.2m, 1m) cần cắt nhỏ nhất, tổng số thanh được dùng để cắt, chiều dài thanh còn dư và phương pháp cắt(tham khảo tại ảnh kết quả).
## Lưu ý
- Ưu tiên chương trình hoạt động trên hệ điều hành windows.
- Chương trình có sử dụng thư viện ngoài là numpy, trong lần đầu tiên chạy chương trình, chương trình sẽ tự động tải về thư viện numpy nếu máy bạn chưa có.
- Trong bước 3, nếu bạn nhập chiều dài thanh bạn muốn cắt dài hơn chiều dài thanh được cắt, chương trình sẽ báo lỗi.
- Chương trình sử dụng đơn vị mét để tính toán.
