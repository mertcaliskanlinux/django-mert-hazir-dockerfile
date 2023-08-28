# Django Software Team Tech Container Projesi

Bu proje, Django web çatısı kullanılarak oluşturulmuş bir örnek proje örneğidir. Projenin amacı, Docker ve Docker Compose kullanarak Django uygulamasını ve bağımlılıklarını içeren konteynerler oluşturmak ve yönetmektir.

## Başlangıç

Bu adımlar, projeyi yerel makinenizde çalıştırmak ve geliştirmek için gereken adımları adım adım açıklar.

### Gereksinimler

- Docker
- Docker Compose
- python3-venv



### Kurulum ve Çalıştırma

Aşağıdaki adımlar, projeyi yerel makinenizde çalıştırmak için gerekli işlemleri adım adım açıklar.

1. Projeyi klonlayın:

```bash
git clone https://github.com/mertcaliskanlnx/django-mert-container.git

cd django-mert-container
```

2. Virtual environment oluşturun:

```bash
python3 -m venv venv
```

3. Virtual environment'ı aktif edin:

```bash
source venv/bin/activate
```

4. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

5. Docker Compose ile bir ağ oluşturun:

    ```bash
    docker network create mynetwork
    ```


6. Docker Compose ile konteynerları ayağa kaldırın:

```bash

docker-compose up -d --build
```

###  konteynerı ayağa kalktıktan sonra, http://localhost:8000 adresinden uygulamaya erişebilirsiniz.
###  konteynerı ayağa kalktıktan sonra, http://localhost:8000/admin adresinden admin paneline erişebilirsiniz.
### admin panel giriş bilgileri:

### username: root
### password: root



7. Konteynerları durdurmak için:

```bash
docker-compose down
```
