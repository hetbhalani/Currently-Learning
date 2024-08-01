
function UserGreeting(props){
    if(props.isLogedin){
        return <h2>Weclome {props.userName}</h2>
    }
    else{
        return <h2>wrong username</h2>
    }
}

export default UserGreeting 