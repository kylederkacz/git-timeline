git-timeline is a simple python library that allows timelines to be built using
git commits.

Example
=======

The following example assumes that your repo directory has been initialized
and is clean for use as a timeline.

build_timeline.py

    >>> from timeline import Timeline
    >>> from datetime import date
    >>> t = Timeline('/Users/myuser/historyofgit')
    >>> t.add_event(date(2005, 4, 3), "Git development begins")
    >>> t.add_event(date(2005, 4, 6), "Official announced")
    >>> t.add_event(date(2005, 4, 18), "First merge of multiple branches")
    >>> t.add_event(date(2005, 6, 16), "2.6.12 Linux kernel release managed by Git")
    >>> t.add_event(date(2005, 7, 26), "Management of Git handed over to Junio Hamano")
    >>> t.add_event(date(2005, 12, 21), "v1.0 released")

Once the timeline is initialized you can view a graphical output of it by
running the following git command from the git repo directory:

    $> git log --graph --all --format=format:'(%cr) %s%d' --date-order --abbrev-commit --date=relative