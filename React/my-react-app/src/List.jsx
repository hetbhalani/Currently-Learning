
function List(){
    // const fruits = ["apple" , "banana", "orange", "watermelon", "grapes"]
    // fruits.sort();

    const fruits = [{name: "apple", cals: 80},
                    {name: "banana", cals: 90},
                    {name: "orange", cals: 100},
                    {name: "watermelon", cals: 110},
                    {name: "grapes", cals: 120},
    ]

    const ListItems = fruits.map(fruits => <li key = {fruits.name}> {fruits.name}</li>)

    return(<ol>{ListItems}</ol>);
}

export default List