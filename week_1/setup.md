Preparing enviornment

I will be using a GCP compute instance for this course. To prepare the enviornment we'll need to setup the following:

* GCP ssh  
* Install Miniconda  
* Install docker & docker-compose  
* Setup an Openai key  
* Install python packages  
* Setup git and github  

**GCP ssh**

```bash
ssh-keygen -t rsa -f ~/.ssh/gcp_new -C [username] -b 2048
cat ~/.ssh/gcp_new.pub >> ~/.ssh/gcp.pub
ssh -i ~/.ssh/gcp [username]@[ip]
ssh-keygen -f "~/.ssh/known_hosts" -R "[ip]"
```

```bash
echo "Host [host-machine]
	HostName [ip]
	User [username]
	IdentityFile ~/.ssh/gcp" | tee ~/.ssh/config 
```

**Install Miniconda** 
Download the latest miniconda installer [here](https://docs.anaconda.com/miniconda/)

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source .bashrc
```

**Install docker & docker-compose**

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

```bash
# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

```bash
sudo docker run hello-world
```

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
```

```bash
# docker compose
sudo wget https://github.com/docker/compose/releases/download/v2.28.1/docker-compose-linux-x86_64 -O /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose 
which docker-compose 
```

**Setup an Openai key**   

Setup an OpenAI key [here](platform.openai.com/api-keys)

```bash
export OPENAI_API_KEY="[OpenAI key]"
```

Check the OpenAI playground for available models.

**Install python packages** 

```bash
conda install tqdm notebook==7.1.2 openai elasticsearch pandas scikit-learn ipywidgets
```

**Setup git and github** 

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub
# add ssh public key to github profile
ssh -T git@github.com
```

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```