# Grupo de Estudos - PLN+IA
This repository, mainly composed of notebooks, is intented for use during the meetings of PLN+AI group of studies conducted by professors Erick Galani Maziero and Paula Christina Cardoso, at Computer Science Department of Federal University of Lavras (DCC/UFLA).

---

## System environment requirements:
1. Python (>= 3.7.0)
2. virtualenv (15.1.0)
3. virtualenvwrapper (4.8.2)
4. pip (9.0.1)

Other versions were not tested, but they may work.

---

## Initial setup
After cloning this repository:

```
git clone https://github.com/egmaziero/PLN-IA.git
```

You may create a virtual environment:
```
mkvirtualenv -p python3 PLN-IA_env
```

Go into the directory of the repository:

```
cd PLN-IA && setvirtualenvproject
```
And install Python requeriments:

```
pip3 install -r requirements.txt
```
---
## Running notebooks

Start the notebooks server:

```
jupyter lab
```

