# Python

Python is a general purpose interpreted programming language. This README is a beginner's guide to the language.

#### A note on standards

To create a standard work flow in the tutorial, UNIX like commands and shell environment will be used. This is because almost all programs are written with this format in mind and then ported to work with Windows. Some of the notable differences are:

1. The difference in prompts.  
   In UNIX environment, the terminal prompt looks like this:  
   `ted@workpc:~ $`  
   Here `ted` represents the username of the current user of the computer, `workpc` is the name of the computer, also known as the host. `~` is the current working directory (aka folder) which in this case is the `home/ted` directory. When there is a change in directory, the prompt will show the path rather than `~`. e.g. `ted@workpc:my-python-projects$` Lastly, `$` shows the privilege of the current user. When `$` is shown, it mean the command is running with normal user privileges and when `#` is shown, it means the command is running with root (aka administrator) permissions.
2. The difference in file paths  
   File paths in UNIX standard always are of the form:  
   `path/to/directory/` and not `C:\\path\\to\\directory>` like they are in Windows. So, when there is a path mentioned in a prompt, adjust yours accordingly.

## Installation

### Windows

- go the [python download page](https://www.python.org/downloads/windows/) and download the latest Python3 stable release.
- Run the executable by double clicking on it.
- On the first window, click on `add python 3.x to PATH` and then click the `install now`
  ![first window](https://www.howtogeek.com/wp-content/uploads/2017/05/ximg_591a18a4aed8c.png.pagespeed.gp+jp+jw+pj+ws+js+rj+rp+rw+ri+cp+md.ic.8f1lV7V3C4.png)
- Proceed with the installation as normal untile you get to this screen:
  ![path limit screen](https://www.howtogeek.com/wp-content/uploads/2017/05/ximg_591a18fea9deb.png.pagespeed.gp+jp+jw+pj+ws+js+rj+rp+rw+ri+cp+md.ic.bRLZBfjf0t.png)  
  Select the option `Disable path length limit`. This will make your life easer later.
- Click `close` and open Command Prompt by clicking on Start and typing "cmd". Select the first option that comes up.  
  type `python3` in the prompt. You should get a prompt with `>>>` at the end.
- You are done.

### Linux

On Linux, python comes pre-installed.

## Installing packages

TODO: add stuff about PIP.
