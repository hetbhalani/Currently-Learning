
function List(props){
    // const fruits = ["apple" , "banana", "orange", "watermelon", "grapes"]
    // fruits.sort();

    // const fruits = [{id: 1, name: "apple", cals: 80},
    //                 {id: 2, name: "banana", cals: 90},
    //                 {id: 3, name: "orange", cals: 130},
    //                 {id: 4, name: "watermelon", cals: 70},
    //                 {id: 5, name: "grapes", cals: 110},
    // ]
    // fruits.sort((a,b) => a.name.localeCompare(b.name)) //sort kre object na names ne
    // fruits.sort((a,b) => b.name.localeCompare(a.name)) //undhu sort krva mate
    // fruits.sort((a,b) => b.cals - a.cals) //numeric ne reverse sort kre
    // fruits.sort((a,b) => a.cals - b.cals) // numeric ne sort kre

    // const lowCalFruits = fruits.filter(fruits => fruits.cals < 100);
    const category = props.category;
    const itemList = props.items;   

    const ListItems = itemList.map(item => <li key = {item.id}> {item.name}: &nbsp; 
    <b>{item.cals}</b></li>);

    return(<>
        <h3>{category}</h3>
        <ol>{ListItems}</ol>
    </>
    );
}

export default List