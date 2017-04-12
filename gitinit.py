#!/usr/bin/python
# coding:utf-8

import subprocess

class gitinit(object):
    def gitinit(self):
        self._doGitInit()
        self._makeGitignoreFile()
        self._makeReadme()

    def _doGitInit(self):
        try:
            result = subprocess.check_output(["git","init"])
        except OSError as e:
            print("OSError: [Errno {0}] {1}".format(e.errno,e.strerror))
        else:
            print(result[:-1])

    def _makeGitignoreFile(self):
        try:
            with open(".gitignore","w") as f:
                print("make .gitignore")
        except OSError as e:
            print("OSError: [Errno {0}] {1}".format(e.errno,e.strerror))
    
    def _makeReadme(self):
        try:
            with open("README.md","w") as f:
                f.write("""
<!--
Visual StudioにおけるMarkdownのプレビュー方法
mac:Command + shift + v
-->
# TOOL_NAME
overview

---
## Description
hogehoge

## Demo
```
>>> command
result
```

## Requirement
* requirement

## Document
#### function name
description  
`name`

## License
本ソフトウェアはMITライセンスに準拠します。  
* [MIT License](http://opensource.org/licenses/mit-license.php)
                """[1:])
                print("make README.md")
        except OSError as e:
            print("OSError: [Errno {0}] {1}".format(e.errno,e.strerror))


def main():
    gi = gitinit()
    gi.gitinit()
    """
    1.git initを実行
    2.gitignoreを作成
    3.README.mdを作成
    """

if __name__ == '__main__':
    main()