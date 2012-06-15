import os, subprocess

def repo_dir(function):
	"""
	A decorator that switches to the root_dir of the timeline object before
	operating and then switches back to the current directory after the work is
	done.
	"""
	def _make_decorator(timeline, *args, **kwargs):
		current_dir = os.getcwd()
		os.chdir(timeline.root_dir)
		function(timeline, *args, **kwargs)
		os.chdir(current_dir)
	return _make_decorator


class Timeline(object):
	"""
	Timeline provides a set of methods to utilize Git as a generic timeline
	system. Dates for the timeline can be specified for any point in the past
	and do not require anything to be committed to the repository.
	"""

	root_dir = None

	def __init__(self, root_dir):
		self.root_dir = os.path.abspath(root_dir)
		if not os.path.exists(self.root_dir):
			raise Exception("The specified repository directory doesn't "
				"exist.")

	@repo_dir
	def init_repo(self):
		# Check if repo is already initialized
		result = subprocess.check_output(["git", "init"])

	@repo_dir
	def add_event(self, event_date, item, branch="master"):
		self._set_event_date(event_date)
		# Switch the branch
		self._switch_branch(branch)
		# Add the item
		result = subprocess.check_output(["git", "commit", "--allow-empty",
			"-m", '%s' % item])

		self._reset_date()

	@repo_dir
	def close_branch(self, event_date, message, branch, merge_into="master"):
		self._set_event_date(event_date)
		self._switch_branch(merge_into)
		result = subprocess.check_output(["git", "merge", "--no-ff", branch, 
										  "-m", '%s' % message])
		self._reset_date()

	def _set_event_date(self, event_date):
		git_date = event_date.strftime("%a %b %d 12:00:00 %Y -0800")
		os.environ['GIT_COMMITTER_DATE'] = git_date
		os.environ['GIT_AUTHOR_DATE'] = git_date

	def _reset_date(self):
		os.environ['GIT_COMMITTER_DATE'] = ""
		os.environ['GIT_AUTHOR_DATE'] = ""

	def _switch_branch(self, branch, auto_create=True, from_branch="master"):
		branches = self._get_branches()
		exists = branch in branches
		if exists and branches[branch]:
			return  # The branch already exists and is active
		command = ['git', 'checkout']
		if auto_create and not exists:
			if branch != from_branch:  # switch to from_branch before branching
				self._switch_branch(from_branch)
			command.append('-b')
		command.append(branch)
		result = subprocess.check_output(command)

	def _get_branches(self):
		branches = {}
		res = subprocess.check_output(["git", "branch"])
		res = res.split("\n")
		for branch in res:
			if branch == "":
				continue
			is_current = branch.startswith("*")
			branches[branch[2:].strip()] = is_current
		return branches
