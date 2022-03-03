# Harvard CS50's Web Development with Django Full Course!
## Lecture 0 - HTML & CSS
```html
<!DOCTYPE html> 
<!-- this is used to tell the browser which version on html is being used. in this case, this lines means html 5 -->

<html lang="en">
    <!-- here, 'lang' is called an html attribute, which helps the browser understand the language in which the page is written -->
    <head>
        <title>
            Tutorial
        </title>

        <!-- the tutor really emphasized on the fact that this link to stylesheet has to be in the head section.
        but after moving it to body section it still worked! any problems? -->
        <!-- "rel" has to be "stylesheet" to make html understand this relation part -->
        <link rel="stylesheet" href="styles.css">
        <style>
            div {
                background-color: orange;
                width: 500px;
                height: 100px;
                padding: 20px;
                margin: 20px;
                /* padding is space of elements inside and margin is space from elements outside */
                /* typing px after a number is mandatory */

                /* the number of different fonts that are going to be mentions one after the other, 
                means that in case a browser didn't support Arial, or it wasn't available for some reason,
                fall back to the next one */
                font-family: Arial , sans-serif;
                font-size: 20px;
                font-weight: bold;        
                border: 3px solid black;   
            }
            table {
                border: 2px solid black;
                border-collapse: collapse;
                text-align: center;
            }
            /* this is a css selector, to apply this style not only to td but also to th as well */
            td, th {
                padding: 5px;
                border: 1px solid black;
            }
        </style>

    </head>
    <!-- you can give style attribute to a parent html tag
    and in the style you are going to write css -->
    <!-- id is giving a unique html tag an identity
    where a class is giving multiple html elements the same identity -->
    <h1 id="welcome_heading"> Welcome to my Webpage!</h1>
    <h1 id="another_heading"> Another Greeting!</h1>
    <h1 class="baz"> Another Greeting!</h1>
    <h1 class="baz"> Another Greeting!</h1>

    <!-- let's instead of inline coding move our style to another place! -->
    <body>
        <!-- we use div in order to separate that section from others. 
        maybe to use custom style or so on -->
        <div>
            Hello, world!
        </div>

        <h2>This is a heading!</h1>
        <h3>This is a smaller heading</h2>
        <h6>The Smallest heading</h6>
        Ordered list:
        
        <!-- this <ol>...</ol> shows that we have an ordered list -->
        <ol>
            <!-- for each list item element we are going to use <li></li> -->
            <li>First Item</li>
            <li>Second Item</li>
            <li>Third Item</li>
            <!-- here, the html tags are nested inside other tags -->
        </ol>

        Unordered List
        <!-- like this, unordered list -->
        <ul>
            <li>First Item</li>
            <li>Second Item</li>
            <li>Third Item</li>
        </ul>

        <!-- image tags has 2 required attributes which are src and alt, others are optional -->
        <img src="Me.jpg" alt="Me!" width="300"><br>
        
        <!-- let's make a link to head to other pages -->
        <!-- a tag is called anchor tag with a mandatory attribute, hyper ref-->
        <a href="https://google.com">Google.com</a><br>
        <a href="image.html">Image</a>

        <!-- let's make a table -->
        <table>
            <!-- table head -->
            <thead>
                <!-- table row -->
                <tr>
                    <!-- table heading -->
                    <th>Ocean</th>
                    <th>Average Depth</th>
                    <th>Max Depth</th>
                </tr>
               
            </thead>
            <tbody>
                <tr>
                    <!-- table data -->
                    <td>Pacific Ocean</td>
                    <td>4000 m</td>
                    <td> 10000 m</td>
                    <td> 10000 m</td>
                    <!-- table rows don't have to have equal columns! -->
                </tr>
                <tr>
                    <td>Atlantic Ocean</td>
                    <td>3000 m</td>
                    <td> 9000 m</td>
                </tr>
            </tbody>
        </table>

        <!-- form is somewhere that users can input some data -->
        <form>

            <div>
            <input type="text" placeholder="Name" name="name">
            <input type="password" placeholder="Password" name="password">
            </div>

            <div>
                Favorite Color: 
                <input name="color" type="radio" value="Red">Red
                <input name="color" type="radio" value="Blue">Blue
                <input name="color" type="radio" value="Green">Green
                <input name="color" type="radio" value="Yellow">Yellow
            </div>

            <div>
                <input name="country" list="countries" placeholder="Country">
                <!-- ths id attribute of the datalist must be identical to input list attribute -->
                <datalist id="countries">
                    <option value="Afghanistan">Description</option>
                    <option value="Iran">afghanistan</option>
                    <option value="USA"></option>
                    <option value="Italy"></option>
                </datalist>
            </div>

            <input type="submit">

        </form>
    </body>
</html>
```
- and also a styles.css:
```css
/* if you want to select something with a specific id, put # before the id
otherwise without the # it will search amongst the html tags to select not ids */
/* similarly in order to give a specific class a specific css style, instead of "#" we use "." */
#welcome_heading, #another_heading {
    color: blue;
    text-align: center;
}
.baz {
    color: rgb(63, 202, 179);
}
```
- there is something in css called Specificity
- it indicates which is section is going to be overwritten by the other
- in CSS the Specificity is as follows:
    1. inline
    2. id
    3. class
    4. type

- CSS Selectors:
    1. a, b  ->  Multiple element Selector
    2. a b  ->  Descendant Selector
    3. a > b  ->  Child Selector
    4. a + b  ->  Adjacent Sibling Selector
    5. [a=b]  -> Attribute Selector
    6. a:b  ->  Pseudoclass Selector
    7. a::b  ->  Pseudoelement Selector

- the difference between "a b" and "a > b" is that the first one is a more general descendant, b can be a's grandchildren and so on
- but a > b is used when b should be a's immediate child and descendant
### Reponsive Design:
- Viewport
- media Queries
- Flexbox
- Grids

### SASS:
webbrowsers can't understand SASS or .scss out of the box. 
we need to compile sass to css. you should install sass on your os and then write in the terminal, we use this line for updates too:<br>
```scss
$color: red;
div {
    color: $color;
}
p {
    color: $color;
}
```
- this will use $color as a variable which you can change easily
```shell
sass variables.scss:variables.css
```
- or you can do:
```shell
sass --watch variables.scss:variables.css
```
- and now with every and each change, sass will automatically apply the changes.
- you can also do the nesting of the html elements without using some of the css selectors
```scss
div {
    ul {
        color: red;
    }
    p {
        h1 {
            color: green;
        }
        color: orange;
    }
}
```
- sass will automatically change this .scss file to a proper css which will look like this:
```css
div ul {
    color: red;
}
div p {
    color: orange;
}
div p h1 {
    color: green;
}
```
- sass also has inheritance:
```scss
%messages {
    font-size: 20px;
    border: 2px;
    margin: 20px;
}
.sucess {
    @extend %message;
    background-color: green;
}
.alert {
    @extend %message;
    background-color: red;
}
.warning {
    @extend %message;
    background-color: yellow;
}
```
## SQL:
```sql
CREATE TABLE <table_name> (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);
INSERT INTO <table_name>
    (origin, destination, duration)
    VALUES ('New York', 'London', 415);
SELECT <cols> FROM <table_name> WHERE
    duration > 500
    OR origin = 'Paris'
    AND destination = 'New York';
UPDATE <table_name>
    SET <col_name> = <value>
    WHERE origin = 'New York'
    AND destination = 'Paris';
DELETE FROM <table_name> WHERE destination = 'Tokyo'
