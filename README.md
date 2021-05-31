# Commit Man

Commit-Man is a version control system that helps the user keep track of and manage different versions of their files.
It features a CLI and a GUI - the complete set of features are available in the CLI, while the GUI features a limited set of features currently (primarily repository browsing functions and viewing diffs across versions).  

A repository can have a .gitignore file that specifies for which files changes are to be ignored across versions (when creating new versions). A special folder (.cm) in each repository stores data for version management.

---

## [CLI](https://github.com/atharva-Gundawar/commit-man) features

- Initializing a repository
- Committing a version and making a new version
- Reverting back to an old version
- Reinitializing in case of corrupted data
- Displaying Logs and Command description

## [GUI](https://github.com/souris-dev/commitman-gui) features

- Viewing commit history
- Browsing the repository
- Viewing diffs of files across versions
- Viewing repository info

---

## Installing

A step by step series of examples that tell you how to get a development env running

>Install from [**PyPi**](https://pypi.org/project/commit-man/):

```bash
 pip install commit-man
```

>Install from [**Source**](https://github.com/atharva-Gundawar/commit-man)

```bash
git clone https://github.com/atharva-Gundawar/commit-man
cd commit-man
python setup.py install
```

---

## The Commands

### Initializing a Repository

>Initialize Commit man in the current directory

```bash
cm init
```

### Committing a version

>Commits curent version of working directory

```bash
cm commit <message>
```

### Reverting back to an old version

>Reverts to an old version of working directory

```bash
cm revert <Commit_Number> [-f | --force]
```

### Reinitialize Commit Man

>Reinitialize Commit man in the current directory

```bash
cm reinit
```

### Displaying Logs

>Displays Log file in a tabular format on the Terminal

```bash
cm showlog
```

### Displaying Command descriptions

>Displays Command descriptions on the Terminal

```bash
cm man
```

---

## Built With

- [Python](https://www.python.org/) - An interpreted high-level general-purpose programming language.
- [Gitignore Parser](https://pypi.org/project/gitignore-parser/) - A spec-compliant gitignore parser for Python 3.5+
- [Docopt](http://docopt.org/) - Command-line interface description language

## Contributing

Please read [CONTRIBUTING](https://github.com/Atharva-Gundawar/Commit-Man/blob/main/PROJECTINFO.md#contributing) for details on our code of conduct, and the process for submitting pull requests.

## Authors

- **Atharva Gundawar** - *Initial work* - [Github handle](https://github.com/Atharva-Gundawar)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
