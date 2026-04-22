from nltk.chat.util import Chat, reflections


dialog = [
	# Tp 1: Basic conversation
	# Basic
	[r"hello$", ["Hello!"]],
	[r"hi$", ["Hi!"]],
	[r"hey$", ["Hey!"]],
	[r"who are you\??$", ["I am a simple chatbot."]],
	[r"my name is (.*)", ["Nice to meet you, %1."]],
	[r"help$", ["Try: programs, modules, subjects, campus, admission, fees, contact."]],
	[r"menu$", ["Menu: type 1 (Project 1 FAQ) or 2 (Project 2 Study) or 3 (Basic)."]],
	[r"1$", ["Project 1: type 1.1 programs, 1.2 modules, 1.3 campus, 1.4 application, 1.5 tuition, 1.6 contact"]],
	[r"2$", ["Project 2: type 2.1 algorithm, 2.2 python, 2.3 java, 2.4 go, 2.5 infra, 2.6 cybersecurity, 2.7 database"]],
	[r"3$", ["Basic: type hello, who are you?, my name is ..."]],

    # project 1: Ynov specific 
	# Programs / Majors (Filières)
	[r"programs\??$", ["We offer different programs. Tell me which major you want (e.g., IT, Business)."]],
	[r"1\.1$", ["Programs: type 'programs' or 'what programs do you have?' or 'program IT'."]],
	[r"what programs do you have\??", ["Programs depend on the campus and intake. Tell me your level and interest."]],
	[r"program (.*)", ["You asked about program '%1'. Do you want subjects, duration, or admission?"]],
	[r"duration$", ["Duration depends on the program. Tell me the program name."]],

	# Modules / Subjects (Modules / Matières)
	[r"modules$", ["Tell me the program and level (example: 'modules IT year 1')."]],
	[r"1\.2$", ["Modules: type 'modules' or 'modules IT year 1'."]],
	[r"modules (.*)", ["For '%1', please specify program + level to get the right list."]],
	[r"subjects (.*)", ["For '%1', specify program + level."]],
	[r"subjects$", ["Tell me the program and level (example: 'subjects IT year 1')."]],

	# Campus
	[r"campus$", ["Which campus/city do you mean?"]],
	[r"1\.3$", ["Campus: type 'campus' or 'campus casablanca' (example)."]],
	[r"where is the campus\??", ["Tell me the campus name (or city) and I will guide you."]],
	[r"campus (.*)", ["For '%1' campus: check the official website page for address and map."]],

	# Admission
	[r"application\??", ["Admission usually requires an application file, and sometimes an interview. What is your level?"]],
	[r"1\.4$", ["Admission: type 'application' or 'how to apply?'"]],
	[r"how to apply\??", ["Tell me your level (high school, bac, bac+2, etc.) and the program you want."]],
	[r"documents$", ["Requirements depend on the program. Tell me the program name."]],
	[r"deadline$", ["Deadlines change each intake. Please check the admissions page or contact the school."]],
	[r"level$", ["Tell me your level (high school, bac, bac+1, bac+2) and the program."]],

	# Fees
	[r"tuition$", ["Fees depend on program, level, and year. Tell me which program and campus."]],
	[r"1\.5$", ["Fees: type 'tuition'."]],
	[r"scholarship", ["Scholarships/aid depend on current offers. Contact admissions for details."]],
	[r"fees$", ["Fees depend on program, level, and year. Tell me which program and campus."]],

	# Contact
	[r"contact$", ["You can contact admissions via the official website contact page."]],
	[r"1\.6$", ["Contact: type 'contact'."]],
	[r"i want to talk to a human$", ["Sure—please contact the admissions office from the website contact page."]],
	[r"email$", ["Please use the official website contact page for the right email."]],
	[r"phone$", ["Please use the official website contact page for the right phone number."]],

    # project 2: Study advice for 1st-year subjects
	# Study / 1st-year subjects
	[r"algorithm$", ["Algorithms: learn variables, loops, arrays, functions, and Big-O."]],
	[r"2\.1$", ["Algorithms: type 'algorithm' or 'sorting'."]],
	[r"sorting$", ["Sorting/search: try linear search, binary search, bubble sort, insertion sort."]],
	[r"search$", ["Search: start with linear search, then binary search on sorted arrays."]],
	[r"big o$", ["Big-O: O(1), O(log n), O(n), O(n log n), O(n^2)."]],
	[r"programming$", ["Programming: write small functions, test with examples, read errors."]],
	[r"debug$", ["Debug tip: print values, simplify input, and test step by step."]],
	[r"2\.2$", ["Python: type 'python' or 'python list' or 'python dict'."]],
	[r"python list$", ["Python list: example -> a = [1, 2, 3] ; a.append(4)"]],
	[r"python dict$", ["Python dict: example -> d = {'a': 1} ; d['b'] = 2"]],
	[r"python$", ["Python: focus on if/else, loops, lists, dicts, functions."]],
	[r"java$", ["Java: focus on types, classes, objects, methods, and OOP basics."]],
	[r"2\.3$", ["Java: type 'java' or 'oop'."]],
	[r"oop$", ["OOP basics: class, object, methods, encapsulation."]],
	[r"go$", ["Go: focus on packages, functions, slices, structs, and error handling."]],
	[r"2\.4$", ["Go: type 'go' or 'go error'."]],
	[r"go error$", ["Go errors: many functions return (value, err). Always check err."]],
	[r"infra$", ["Infra: basics of OS + networking (IP, DNS, HTTP)."]],
	[r"2\.5$", ["Infra: type 'infra' or 'dns' or 'http'."]],
	[r"dns$", ["DNS maps a domain name to an IP address."]],
	[r"http$", ["HTTP is the protocol used by web browsers and servers."]],
	[r"cybersecurity$", ["Security: strong passwords, updates, and avoid phishing."]],
	[r"2\.6$", ["Security: type 'cybersecurity' or 'phishing'."]],
	[r"phishing$", ["Phishing is a fake message to steal your info. Always verify links."]],
	[r"database$", ["Databases: tables, primary keys, relations, and SQL SELECT/WHERE/JOIN."]],
	[r"2\.7$", ["Databases: type 'database' or 'sql' or 'join'."]],
	[r"sql$", ["SQL basics: SELECT ... FROM ... WHERE ..."]],
	[r"join$", ["JOIN combines rows from 2 tables using a key."]],

	[r"(.*)", ["I don't understand."]],
]


chatbot = Chat(dialog, reflections)

if __name__ == "__main__":
	chatbot.converse()
