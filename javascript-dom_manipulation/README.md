### Hey peer,

If you wanna review my tasks DOM Manipulation here the command to execute in your terminal.
This will only copy the DOM manipulation directory inside the REPO.

```bash
git clone --filter=blob:none --no-checkout https://github.com/vlldnt/holbertonschool-higher_level_programming.git && 
cd holbertonschool-higher_level_programming && 
git sparse-checkout init --cone &&
git sparse-checkout set javascript-dom_manipulation &&
git checkout &&
cd javascript-dom_manipulation
```
***[Go Live](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)*** and test all 9 HTMLs.


#### Here’s a summary of the 9 tasks
0. Change the header text color to red.
1. Change the header text color to red when clicked.
2. vAdd the .red class to the header when clicked.
3. Toggle between .red and .green classes on the header when clicked.
4. Add an <li> element to a list when clicked.
5. Fetch and display a Star Wars character's name via an API.
6. List Star Wars movie titles via an API.
7. Display "Hello" in a specific language via an API.
8. Add, remove, and clear list items via clicks.

**Thanks**