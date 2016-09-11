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
    var key, value, filter_string;
    var filter_arr = [];
    for (key in filters){
        filter_arr.push(key + "=" + filters[key]);
    }

    if (filters){
        filter_string = "?" + filter_arr.join("&");
    }
    else {
        filter_string = "";
    }

    return $.ajax({
        url: "http://127.0.0.1:8000/" + model.toLowerCase() + "/" + filter_string,
        success: function(data) {
            console.log(data);
            return data;
        },
        error: function(data) {
            console.log("There was an error with your FOP request. Go hike a mountain.");
        }
    });
}

const store = createStore(reducers)
const reduxHistory = syncHistoryWithStore(browserHistory, store)

class Index extends React.Component{

	render(){
        window.foppie = foppie;
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
