// import UserGreeting from "./UserGreeting.jsx";
import List from "./List";

function App() {
    const fruits = [{id: 1, name: "apple", cals: 80},
      {id: 2, name: "banana", cals: 90},
      {id: 3, name: "orange", cals: 130},
      {id: 4, name: "watermelon", cals: 70},
      {id: 5, name: "grapes", cals: 110},
  ];

  return(  
    <>
        {/* <UserGreeting isLogedin={true} userName="Het Bhalani"></UserGreeting> */}
        
        <List items = {fruits} category = "Fruits"></List>
    </>
  );
}

export default App
