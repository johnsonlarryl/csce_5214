<!-- ABOUT THE PROJECT -->

## About The Project

TBD

| Type                | Sub Type | Algorithm                                      |
|---------------------|----------|------------------------------------------------|
| Supervised Learning | NLP      | [CNN](text_classification/) |

### Built With

This section lists all major frameworks/libraries used to bootstrap this project.

* [![Python][Python.org]][Python-url]
* [![Jupyter][Jupyter.org]][Jupyter-url]
* [![Miniconda][Miniconda.com]][Miniconda-url]
* [![Docker][Docker.com]][Docker-url]
* [![AWS][AWS.Amazon.com]][AWS-url]



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Following the instructions below should get you up and running and quickly as possible without googling around to run
the code.

### Prerequisites

Below is the list things you need to use the software and how to install them. Note, these instructions assume you are
using a Mac OS. If you are using Windows you will need to go through these instructions yourself and update this READ
for future users.

1. pyenv
   ```sh
    brew update
    brew install pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
    echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   ```
2. python
   ```sh
    pyenv install 3.9.5   
    pyenv global 3.9.5 
   ```

3. poetry
   ```sh
   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
   ```

4. miniconda
   ```sh
   cd /tmp
   curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
   bash Mambaforge-$(uname)-$(uname -m).sh
   ```

5. Restart new terminal session in order to initiate mini conda environmental setup

6. Git LFS
   ```sh
   brew install wget
   git lfs track "*.zip"
   git lfs track "*.gz"
   git add .gitattributes
   ```
   
8. [Docker, including docker-compose](https://docs.docker.com/engine/install/)

9. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

### Installation

Below is the list of steps for installing and setting up the app. These instructions do not rely on any external
dependencies or services outside of the prerequisites above.

1. Clone the repo
   ```sh
   git clone git@github.com:fall2023csce5214/text_classification.git
   ```
2. Install notebook
   conda env create -f environment.yml
   conda activate text_classification
3. Build Docker Image (Note, you should be in the same dire)
   ```sh
   docker-compose build
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->

## Usage

In order to view or execute the various notebooks run the following command on any of the sub folders in this directory.

Here is an example to launch the Text Classification Notebook.

```sh
jupyter notebook
```

Once inside the
notebook [use the following link](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html)
on examples of how to use the notebook.

Here is an example to launch docker to run the unit test on the command line.

```sh
docker-compose up -d
docker-compose exec text-classification-web-service bash
```

Here is an example to launch docker to populate the database and launch the web service.
```sh
docker-compose up -d
docker-compose logs -f text-classification-web-service
```

Then hit the following URL to test the web service.  Note, wait until the web service starts.  You will see a message like the following:
```
INFO:     Will watch for changes in these directories: ['/lstm']
INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
INFO:     Started reloader process [142] using statreload
INFO:     Started server process [146]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

[Text Classification using SpaCy](https://www.kaggle.com/code/poonaml/text-classification-using-spacy/notebook)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact
[Akhila Siripurapu](mailto:akhila1578@gmail.com)
<br>
[Larry Johnson](mailto:johnson.larry.l@gmail.com)
<br>

Project Link: [https://github.com/fall2023csce5214/text_classification/](https://github.com/fall2023csce5214/text_classification/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Jupyter-url]:https://jupyter.org

[Jupyter.org]:https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white

[Python-url]:https://python.org

[Python.org]:https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

[Miniconda-url]:https://docs.conda.io/

[Miniconda.com]:https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white

[Docker-url]:https://www.docker.com/

[Docker.com]:https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white

[AWS-url]:https://aws.amazon.com/

[AWS.Amazon.com]:https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white
