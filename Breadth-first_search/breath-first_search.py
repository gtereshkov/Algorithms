from collections import deque

graph = {}
graph["gianna"] = ["bob", "alex"]
graph["alex"] = ["gianna", "sam", "tim", "stewart"]
graph["bob"] = ["michael", "tim", "gianna"]
graph["michael"] = ["bob, coop"]
graph["tim"] = ["tommy", "alex", "bob"]
graph["sam"] = ["samuel", "alex"]
graph["samuel"] = ["tommy", "coop", "stewart", "sam"]
graph["tommy"] = ["tim", "samuel"]
graph["coop"] = ["michael", "samuel", "noon"]
graph["noon"] = ["coop", "frank", "stewart", "jill"]
graph["frank"] = ["noon"]
graph["jill"] = ["noon"]
graph["stewart"] = ["noon", "samuel", "alex"]

def name_is_palindrome(name):
	eman = ''
	for i in name:
		eman = i + eman;
	if name == eman:
		return True
	else:
		return False

def search(name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if name_is_palindrome(person):
				print(person + " is an owner of palindrome-name!")
				return True
			else:
				search_queue +=graph[person]
				searched.append(person)
	return False;

search("sam");