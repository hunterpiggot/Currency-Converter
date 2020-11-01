### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
* The difference between Python and JavaScript is Python a server sided language and JavaScript is a for frontend development. This means that JavaScript is to make a page functional and do certain things. Python tells where links to send you, have logic in the back and and transfer variables, save data and use it for later.
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
* if dict.has_key('c')
  * if  'c' in dict:
- What is a unit test?
  * A unit test, tests a specific function as its own. It is just a single function while not tying any other functionality of what you're testing.
- What is an integration test?
  * An integration test tests if multiple parts of a functionality works together. This is usually after a unit test because a unit tests the components of the function that is being tested.
- What is the role of web application framework, like Flask?
  * This is to make it easier to make a functional website and easily add routes in the URL. It can be done without these frameworks, but these will make things far easier.
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
* If you use a query param, this is usually used so you do not have to hard code every possible route. If you are not using a query param, this means that the link did not require any information that would change the page. An example of this would be reddit. If you are looking for something in a subreddit, you will type something in and it will load things that fit the param. But if you are at the home page, it is only loading things that everyone will see and is not specific you. 
- How do you collect data from a URL placeholder parameter using Flask?
  * '/something<parameter>'
  * def a_func(parameter):
- How do you collect data from the query string using Flask?
  * request.args.get('something')
- How do you collect data from the body of the request using Flask?
  * request.json
- What is a cookie and what kinds of things are they commonly used for?
  * cookies are used to store data such as if you are logged in, what you clicked, what you have visited, etc.
- What is the session object in Flask?
  * It is a dictionary that can store a lot of data the entire time the paged is pulled up. As soon as you close the tab, it is all forgotten. 
- What does Flask's `jsonify()` do?
  * Turns data into JSON notation so it is easy to use
