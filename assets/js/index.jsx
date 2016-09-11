import React from "react"
import ReactDOM from "react-dom"
import { Router, Route, browserHistory } from "react-router"
import { Provider } from "react-redux"
import { syncHistoryWithStore, routerReducer } from "react-router-redux"
import { createStore, combineReducers } from "redux"
import $ from 'jquery';

function reducer(state, action){
	if (state == undefined) {
		return {}
	}
	return state
}
var reducers = combineReducers({
	app: reducer,
	routing: routerReducer
})

function foppie(model, filters){
    $.ajax({
        url: "http://127.0.0.1:8000/#{}/"
    }).then(
        function(data){
            console.log("werd dude", data);
        }
    );
    console.log("foolala", thing);
}


const store = createStore(reducers)
const reduxHistory = syncHistoryWithStore(browserHistory, store)

class Index extends React.Component{

	render(){
        var script = document.createElement('script');
        script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js";
        document.getElementsByTagName('head')[0].appendChild(script);
		return <div>Index!</div>
	}
}
class App extends React.Component {
	render(){
		return (
			<Provider store={store}>
				<Router history={reduxHistory}>
					<Route path="/" component={Index}/>
				</Router>
			</Provider>
		)
	}	
}

ReactDOM.render(<App/>, document.getElementById("app"))
