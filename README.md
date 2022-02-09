# Review Genie

Complete amazon product review analysis under one hood. Review Genie is a web application that helps users to understand more and provides insights about fellow customers and users regarding their opinion and thoughts on a certain product the user wants to purchase on Amazon(IN).


## Summary of Contents

<details open="open">
  <ol>
    <li>
      <a href="#built-with">Built With</a>
    </li>
    <li><a href="#problem-addressed">Problem Addressed</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#run-it">Run it</a></li>
      </ul>
    </li>
    <li><a href="#example">Example</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#new">New!</a></li>
    <li><a href="#coming-up">Coming up</a></li>
    
  </ol>
</details>

### Built With
1. Python
2. Flask
3. Azure Congintive servies
4. Plotly
5. Selenium
6. Beautiful Soup
7. Bootstrap


## Problem Addressed
Helping customers understand about the product they want to buy on Amazon through a visual representation.

## Getting Started
### Prerequisites
- To install the required prerequisite modules, just run
``` pip install -r requirements.txt```
- Install a recent chrome driver and save it in the same folder as this project. Change the path of the chrome driver to your path in ```getData.py line 10```


### Run it
After all the required files and modules are downloaded. Run the command 
<br>
```python3 app.py```
<br>
- Then the home page appears on your browser
- On the home page, you fill find a box which states "Enter ASIN number",
there in that box you need to type the ASIN code of the product.
- Click on submit

<br>
You are good to go!! The page that you get redirected to has all the information you need.

## Example
Here is a demo on how to run the application,
![demo]()

## Results
### Home/Landing page:
![home](https://user-images.githubusercontent.com/53928899/153270456-e228b959-aa04-4f1d-9ff6-a42355445284.png)




## New!
Opinion mining of the comments of the user.


## Coming up
### Personalized experience
- Add user login system, so that they can have a personlaized experience where they can track their activity.
### New features
- Add more features to the dashboard such as word cloud of key words.



