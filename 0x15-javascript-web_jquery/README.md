![jqueryLol](https://github.com/Obony/alx-higher_level_programming/assets/117737538/6f3686f7-208a-4a4d-9d7b-2a72867c3cf4)

# JavaScript - Web jQuery
- [x] Front-end
- [x] JavaScript

## Resources Used
* [What is JavaScript?]
* [Selector]
* [Get and set content]
* [Manipulate CSS classes]
* [Manipulate DOM elements]
* [API]
* [Introduction To Ajax](https://jquery-tutorial.net/ajax/introduction/)
* [GET & POST request]
* [JQuery Ajax Tutorial #1 - Using AJAX & API’s]
* [What went wrong? Troubleshooting JavaScript]
* [JQuery]
* [JQuery API]
* [JQuery Ajax]

## Learning Objectives
* Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
* How to select HTML elements in JavaScript
* How to select HTML elements with JQuery
* What are differences between ID, class and tag name selectors
* How to modify an HTML element style
* How to get and update an HTML element content
* How to modify the DOM
* How to make a GET request with JQuery Ajax
* How to make a POST request with JQuery Ajax
* How to listen/bind to DOM events
* How to listen/bind to user events

## Import JQuery
```JS
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

This was the preparatory project learning how to manipulate the DOM with jQuery
before implementing it into our AirBnb project.


## Tests :heavy_check_mark:

* [tests](./tests): Folder of HTML files for testing DOM manipulation scripts.

## Tasks :page_with_curl:

* **0. No jQuery**
  * [0-script.js](./0-script.js): JavaScript script that uses `document.querySelector`
  to update the text color of the HTML tag `HEADER` to red (`#ff0`).

* **1. With jQuery**
  * [1-script.js](./1-script.js): JavaScript script that uses jQuery to update the
  text color of the HTML tag `HEADER` to red (`#ff0`).

* **2. Click and turn red**
  * [2-script.js](./2-script.js): JavaScript script that uses jQuery to update the text color
  of the HTML tag `HEADER` to red (`#ff0`) when the user clicks on the tag `DIV#red_header`.

* **3. Add `.red` class**
  * [3-script.js](./3-script.js): JavaScript script that uses jQuery to add the class
  `.red` to the HTML tag `HEADER` when the user clicks on the tag `DIV#red_header`.

* **4. Toggle classes**
  * [4-script.js](./4-script.js): JavaScript script that uses jQuery to toggle the class
  of the HTML tag `HEADER` between `.red` and `.green` when the user clicks on the tag
  `DIV#red_header`.

* **5. List of elements**
  * [5-script.js](./5-script.js): JavaScript script that uses jQuery to add a `LI`
  element to a list when the user clicks on the tag `DIV#add_item`.
  * Adds the element `<li>Item</li>` to `UL.my_list`.

* **6. Change the text**
  * [6-script.js](./6-script.js): JavaScript script that uses jQuery to update the text
  of the HTML tag `HEADER` to "New Header!!!" when the user clicks on the tag
  `DIV#update_header`.

* **7. Star wars character**
  * [7-script.js](./7-script.js): JavaScript script that uses jQuery to fetch the Star
  Wars API `https://swapi.co/api/people/5/?format=json` and display the name in the HTML
  tag `DIV#character`.

* **8. Star Wars movies**
  * [8-script.js](./8-script.js): JavaScript script that uses jQuery to fetch and list
  all movie titles from the Star Wars API `https://swapi.co/api/films/?format=json`.
  * Titles are listed in the HTML tag `UL#list_movies`.

* **9. Say Hello!**
  * [9-script.js](./9-script.js): JavaScript script that uses jQuery to fetch and display
  how to say "Hello" in French using the API
  `https://fourtonfish.com/hellosalut/?lang=fr`.
  * Displays the translation in the HTML tag `DIV#hello`.
  * Works when imported in the `HEAD` tag.

* **10. No jQuery - document loaded**
  * [100-script.js](./100-script.js): JavaScript script that uses `document.querySelector`
  to update the text color of the HTML tag `HEADER` to red (`#ff0`).
  * Works when imported in the `HEAD` tag.

* **11. List, add, remove**
  * [101-script.js](./101-script.js): JavaScript script that uses jQuery to add, remove,
  and clear `LI` elements from a list based on user click input.
  * Adds a new element when the user clicks `DIV#add_item`.
    * Adds `<li>Item</li>` to the HTML tag `UL.my_list`.
  * Removes the last element when the user clicks `DIV#remove_item`.
  * Clears all elements when the user clicks `DIV#clear_list`.
  * Works when imported in the `HEAD` tag.

* **12. Say hello to everybody!**
  * [102-script.js](./102-script.js): JavaScript script that uses jQuery to fetch and
  display how to say "Hello" in a given language using the API
  `https://www.fourtonfish.com/hellosalut/hello/`.
  * Fetches the translation for the language entered in the HTML tag `INPUT#language_code`.
  * Fetches the translation when the user clicks on the HTML tag `INPUT#btn_translate`.
  * Displays the translation in the HTML tag `DIV#hello`.
  * Works when imported in the `HEAD` tag.

* **13. And press ENTER**
  * [103-script.js](./103-script.js): JavaScript script that uses jQuery to fetch and
  display how to say "Hello" in a given language using the API
  `https://www.fourtonfish.com/hellosalut/hello/`.
  * Identical to [102-script.js](./102-script.js) except that the tranlsation is fetched
  when either the user clicks on the HTML tag `INPUT#btn_translate` or presses `ENTER`
  when hovering over the tag `INPUT#language_code`.
