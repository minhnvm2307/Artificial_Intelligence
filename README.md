Dưới đây là tổng hợp các kiến thức về công thức Fourier Transform, phân loại theo từng dạng tín hiệu và ứng dụng:

---

### **1. Fourier Transform cho tín hiệu liên tục không tuần hoàn (CTFT)**
- **Công thức phân tích (Biến đổi thuận):**  
  $$
  X(\omega) = \int_{-\infty}^{\infty} x(t) e^{-j\omega t} \, dt
  $$
- **Công thức tổng hợp (Biến đổi ngược):**  
  $$
  x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(\omega) e^{j\omega t} \, d\omega
  $$
- **Điều kiện tồn tại:**  
  $$
  \int_{-\infty}^{\infty} |x(t)| \, dt < \infty \quad (\text{Tích phân hội tụ tuyệt đối})
  $$
- **Ứng dụng:** Phân tích phổ tín hiệu liên tục (ví dụ: âm thanh analog).

---

### **2. Fourier Transform cho tín hiệu rời rạc không tuần hoàn (DTFT)**
- **Công thức phân tích:**  
  $$
  X(\omega) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}
  $$
- **Công thức tổng hợp:**  
  $$
  x[n] = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(\omega) e^{j\omega n} \, d\omega
  $$
- **Điều kiện tồn tại:**  
  $$
  \sum_{n=-\infty}^{\infty} |x[n]| < \infty \quad (\text{Tổng hội tụ tuyệt đối})
  $$
- **Ứng dụng:** Xử lý tín hiệu số (ví dụ: lọc số).

---

### **3. Chuỗi Fourier cho tín hiệu liên tục tuần hoàn (CFS)**
- **Biểu diễn chuỗi:**  
  $$
  x(t) = \sum_{k=-\infty}^{\infty} X_k e^{j k \omega_0 t}
  $$
  với \(\omega_0 = \frac{2\pi}{T}\) (tần số cơ bản).
- **Công thức hệ số:**  
  $$
  X_k = \frac{1}{T} \int_{0}^{T} x(t) e^{-j k \omega_0 t} \, dt
  $$
- **Ứng dụng:** Phân tích mạch điện xoay chiều.

---

### **4. Chuỗi Fourier rời rạc (DFS) cho tín hiệu rời rạc tuần hoàn**
- **Biểu diễn chuỗi:**  
  $$
  x[n] = \sum_{k=0}^{N-1} X_k e^{j \frac{2\pi}{N} k n}
  $$
- **Công thức hệ số:**  
  $$
  X_k = \frac{1}{N} \sum_{n=0}^{N-1} x[n] e^{-j \frac{2\pi}{N} k n}
  $$
- **Ứng dụng:** Xử lý tín hiệu tuần hoàn rời rạc.

---

### **5. Biến đổi Fourier rời rạc (DFT)**
- **Công thức DFT (thuận):**  
  $$
  X[k] = \sum_{n=0}^{N-1} x[n] e^{-j \frac{2\pi}{N} kn}, \quad k = 0, 1, ..., N-1
  $$
- **Công thức IDFT (ngược):**  
  $$
  x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{j \frac{2\pi}{N} kn}, \quad n = 0, 1, ..., N-1
  $$
- **Ứng dụng:** Xử lý tín hiệu số hữu hạn (ví dụ: FFT trong âm thanh số).

---

### **6. Tính chất quan trọng của Fourier Transform**
1. **Tuyến tính:**  
   $$
   a x_1(t) + b x_2(t) \leftrightarrow a X_1(\omega) + b X_2(\omega)
   $$
2. **Dịch thời gian:**  
   $$
   x(t - t_0) \leftrightarrow X(\omega) e^{-j\omega t_0}
   $$
3. **Dịch tần số (Điều chế):**  
   $$
   x(t) e^{j\omega_0 t} \leftrightarrow X(\omega - \omega_0)
   $$
4. **Tích chập:**  
   $$
   x(t) * h(t) \leftrightarrow X(\omega) H(\omega)
   $$
5. **Đạo hàm:**  
   $$
   \frac{d x(t)}{dt} \leftrightarrow j\omega X(\omega)
   $$

---

### **7. Mối liên hệ giữa các biến đổi**
- **CTFT ↔ DTFT:** Lấy mẫu tín hiệu liên tục → tín hiệu rời rạc.
- **DTFT ↔ DFT:** DFT là DTFT được lấy mẫu tại các tần số rời rạc.
- **CFS ↔ CTFT:** Tín hiệu tuần hoàn → Phổ vạch (dirac delta).

---

### **8. Ứng dụng thực tế**
- **Nén dữ liệu:** JPEG (DCT), MP3 (Biến đổi Fourier ngắn - STFT).
- **Truyền thông:** Điều chế tín hiệu (QAM, OFDM).
- **Xử lý ảnh:** Lọc nhiễu, phát hiện biên cạnh.

---

### **Tóm tắt sự khác biệt chính**
| **Loại**          | **Tín hiệu đầu vào** | **Phổ**           | **Công thức**         |
|--------------------|-----------------------|-------------------|-----------------------|
| **CTFT**           | Liên tục, không tuần hoàn | Liên tục         | Tích phân vô hạn     |
| **DTFT**           | Rời rạc, không tuần hoàn | Liên tục (tuần hoàn 2π) | Tổng vô hạn         |
| **CFS**            | Liên tục, tuần hoàn  | Rời rạc           | Chuỗi vô hạn        |
| **DFT**            | Rời rạc, hữu hạn     | Rời rạc, hữu hạn  | Tổng hữu hạn        |

Hy vọng tổng hợp này giúp bạn hệ thống hóa kiến thức về Fourier Transform! Hãy luyện tập với ví dụ cụ thể để hiểu sâu hơn.