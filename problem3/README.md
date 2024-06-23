# 3. Propose a JavaScript implementation of the mechanism for waiting for an element in a DOM tree.

## Solution

If to be honestly i haven't work with js closely, but here somethig that AI advice me. 

``` javascript
setTimeout(() => {
        const element = document.createElement('div');
        element.className = 'test-element';
        document.body.appendChild(element);
    }, 500);
```

It isn't seem like we do neccesery check.

But then it gives this

```javascript

function waitElement(cssSelector, timeout = 4000) {
    return new Promise((resolve, reject) => {
        const interval = 100; // Частота проверки
        const endTime = Date.now() + timeout;

        function check() {
            const element = document.querySelector(cssSelector);
            if (element) {
                resolve(element);
            } else if (Date.now() < endTime) {
                setTimeout(check, interval);
            } else {
                reject(new Error(`Element with selector "${cssSelector}" not found within ${timeout}ms`));
            }
        }

        check();
    });
}

```

and run it with 

``` javascript
waitElement('.my-element', 5000)
    .then(element => {
        console.log('Element found:', element);
    })
    .catch(error => {
        console.error('Element not found:', error);
    });
```

## But!

I understand that it isn't my solution, but i think that we must to understand its output, such as legacy code in real life projects. And nevertheless we offten use ready funcs from frameworks such selenium driven or cypress built in methods.


