# **CAN-Bus-with-Python**


>"CAN Bus 1980'li yıllarda Robert BOSCH tarafından geliştirilmiş bir iletişim protokoldür. Hızlı ve hata oranının çok düşük olması sebebi ile günümüzde otomotiv sektöründe yaygın olarak kullanılmaktadır. 
Diğer iletişim protokollerine göre farkı; elektronik birimlerin adreslendiği master-slave metodu yerine mesajların adreslendiği multimaster bir yapıda olmasıdır."


>"**Siz de kendi bilgisayarınızda sanal bir CAN Bus hattı simüle ederek çalışmalarınızı gerçekleştirebilirsiniz**"


### NOT: CAN Bus hattı linux işletim sistemi üzerinde simüle edilmektedir. Eğer linux işletim sistemi kurulu bir bilgisayarınız yoksa Windows üzerine virtual machine olarak ubuntu kurarak kolayca çalıştırabilirsiniz.





## STEP 1


```bash
sudo modprobe vcan
```
```bash
sudo ip link add dev vcan0 type vcan
```
```bash
sudo ip link set up vcan0 
```

>"İlk komut satırı ile bilgisarınızda bir nevi can sanal makinası kurdunuz. İkinci komut satırı ile bu sanal makinaya vcan0 adında bir CAN Bus hattı bağlanmanızı sağlar. Üçünü satır ile oluşturduğunuz sanal can hattı etkinleştirilir.  "


## **STEP 2**

>"Artık sanal CAN hattınızı dinleyebilirsiniz. Yapmanız gereken yeni bir teminal açarak aşağıdaki kodu yazmanız"

```bash
candump vcan0
```

>"İlk CAN mesajınızı terminal üzerinden gönderebilirsiniz"

```bash
cansend vcan0 001#1234567890ABCDEF
```

>"Yukarıda verilen kod satırı ile can0 hattına 001 adresli 123456789ABCDEF mesajı göndermiş olduk."

![Screenshot2021-12-28 21_40_22](https://user-images.githubusercontent.com/81256525/147609388-a0cce51c-718a-43bb-af54-442ceaa3c8ec.png)


## STEP 3 

>"Aşağıdaki komut ile tek tek mesaj yollamak yerine bilgisayarın sizin için rastgele can mesajları göndermesini sağlayabilirsiniz"

```bash
cangen vcan0
```



https://user-images.githubusercontent.com/81256525/147609461-42dbc17c-28bb-40a7-af19-00579800d0c8.mp4



## STEP 4 

>"python ile CAN Bus operasyonları yapabilmek için python-can kütüphanesini kuralım"
```bash
pip install python-can
```


>"Şimdi herhangi bir python dosyası oluşturup aşağıdaki kod ile can hattını dinleyerek yazdırabilirsiniz"

```python
import can 

bus = can.interface.Bus(bustype = "socketcan", channel= "vcan0", bitrate = 250000)

while True:
    msg = bus.recv()
    print(msg)
```


https://user-images.githubusercontent.com/81256525/147609536-9592b0be-bcc1-4c73-9ee2-1026977d94ab.mp4





## SON

>"Merhaba ben YEC, umarım yardımcı olmuştur. Repoya eklediğim örnek kodları inceleyip python kullanarak mesaj gönderme, alma ve filtreleme gibi birçok farklı çalışma yapabilirsiniz. Linkedin hesabımdan beni takip edebilir ve sorularınızı sorabilirsiniz."

[Linkedin](https://www.linkedin.com/in/yunus-emre-co%C5%9Fkun-84a330202/)













