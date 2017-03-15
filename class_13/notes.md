Task:

1. Add ajax CDN to login page.
2. Create functionality for button click and execution of POST request.
3. In the Django login function,
	- Add csrf_exempt
	- Replace all render() with HttpResposne()
	- convert the whole login function to an API
4. Finally, while staying on the same login page, the user should be able to login and in case of faliure/invalid login, the page shouldn't be changed. instead reset the form and prompt the user to try again.