[TR]
# FlipHtml5BookScraper

Yazmış olduğum bu aracın amacı FlipHTML5 kullanılarak oluşturulan kütüphanelerde yer alan kitapların slayt halinde bulunan görsellerini PDF olarak kaydetmenizi sağlamaktır.

Kullanım için ilk olarak bu tür sitelerde İncele kısmı maalesef aktif değildir. Bu yüzden inceleme kısmını açmak için [link1](https://chromewebstore.google.com/detail/absolute-enable-right-cli/jdocbkpgdakpekjlhemmfcncgdjeiika?hl=en-US&utm_source=ext_sidebar) Asagidaki Gorselde Yer alan eklentiyi:
![alttext](https://imgur.com/a/3xWITEf) linkteki eklentiyi indiriyoruz. Daha sonrasında inen eklentiyi sayfa üzerinde [enable copy] ve [Absolute Mod] seçeneklerini aktif ediyoruz:
![Gorsel2](https://imgur.com/a/5Yt1Qfx)

Bu seçenekler aktif olduğunda istediğimiz kitabın sayfasını incele bölümünden:
![Gorsel3](https://imgur.com/BGfHjVW)
Iilk olarak yukarıda yer alan görseldeki, kırmızı ok ile gösterilen element seçici seçmekteyiz. Sonrasında siyah ok ile gösterilen indirmek istediğimiz sayfanın üstüne getirmeliyiz.
![Gorsel4](https://imgur.com/WIylMSx)
İstediğimiz sayfanın görsel linkine ulaşmaktayız, bundan sonrası için:
![Gorsel5](https://imgur.com/Sd2xjWS)  tam link adresini kopyalıyoruz.

Gerekli linki aldıktan sonra ve indirmek istediğiniz kitap sayfasının son sayfa sayısını main.py dosyasının içinde yer alan end değişkenine atama yapıyoruz.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki paketleri yüklemeniz gerekecek:

- Pillow
- requests


Bunları pip ile yükleyebilirsiniz:
```bash
pip install -r requirements.txt
```
Depoyu klonlayın:
```bash
git clone https://github.com/yourusername/your-repo.git
```
```bash
cd your-repo
```
Gereksinimleri yükleyin:
```bash
pip install -r requirements.txt
```
Ana script'i çalıştırın:
```bash
python {YOURPATH}/main.py
```

[ENG]

# FlipHtml5BookScraper
The purpose of this tool is to allow you to save the images of books displayed in slide format in libraries created using FlipHTML5 as a PDF.

## Requirements

To run this project, you'll need to install the following packages:

- Pillow
- requests

You can install them using pip:
```bash
pip install -r requirements.txt
```
Clone the repository:
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```
Install the requirements:
```bash
pip install -r requirements.txt
```
Run the main script:

```bash
python {YOURPATH}/main.py
```
