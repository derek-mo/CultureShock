//Final JavaScript

const getFacts = async function () {
// making a network request = asking for resources outside of your reach, so there's no telling how long until you get the stuff back
// browser asks flask server for stuff

    const result = await fetch("http://127.0.0.1:5000/facts")    // returns the """array"""
    console.log(result)
    return await result.json()      // takes the response object, reads it, and converts the body into json- smn javascript can use
    
}

const quoteToHTML = function(country) {
// quote obj should have the fields quote and author
// TODO: turn quote obj into some html container 

    //factTable = document.getElementById("fact-table");
    // for (let i = 0; i < quote.length; i++)
    // {
    //     let li = document.createElement("li");
    //     li.innerText = item;
    //     list.appendChild(li);
    // }
    
    return `
        <div class="container">
        <div class="table-responsive-lg">
            <table class="table table-light">
                <tbody>
                    <tr>
                        <td>
                            ${country.factlist[0]}
                        </td>
                    </tr> 
                    <tr>
                        <td>
                            ${country.factlist[1]}
                        </td>
                    </tr> 
                    <tr>
                        <td>
                            ${country.factlist[2]}
                        </td>
                    </tr> 
                </tbody>     
            </table> 
        </div>
    </div>
        ` 
      



        //return "<div>"+quote.fact+"</div>";
}

const generateQuote = async function() {
    
    // javascript rep of the div in html, doc is the DOM
    const factTable = document.getElementById('fact-table')
    
    // a check for whether the div exists
    if (factTable)
    {
        factTable.innerHTML = "<h1> Hello! </h1>"
    }

    console.log({factTable})
    
    
    
    const countries = [
    {
        factlist : ["Fact1","Fact2","Fact3"] ,
        author: "Albus Dumbledore",
        fact: "Did you know, bacon is tasty?"

    },
    
];

    factTable.innerHTML = quoteToHTML(countries[0])

    const fact = await getFacts()     // invoking getFacts
    console.log(fact)           // print result


    return

    let arrayIndex = Math.floor(Math.random() * quotes.length);
    document.getElementById("quotes").innerHTML = quotes[arrayIndex].quote;
    document.getElementById("author").innerHTML = quotes[arrayIndex].author;
    document.getElementById("fact").innerHTML = quotes[arrayIndex].fact;


    //Syntax : arrayVariableName[index]
console.log(quotes[3].quote); // If you want to know what a man’s like, take a good look at how he treats his inferiors, not his equals.
console.log(quotes[3].author); // Sirius Black

}
window.onload = function() {
    generateQuote();
    //document.getElementById("generate").addEventListener('click', generateQuote);
}
