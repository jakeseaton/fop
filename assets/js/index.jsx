import React from "react"
import ReactDOM from "react-dom"
import { Router, Route, browserHistory } from "react-router"
import { Provider } from "react-redux"
import { syncHistoryWithStore, routerReducer } from "react-router-redux"
import { createStore, combineReducers } from "redux"
import Planner from "./components/Planner.jsx"

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

const store = createStore(reducers)
const reduxHistory = syncHistoryWithStore(browserHistory, store)

class Index extends React.Component{
	render(){
		return <div className="container-fluid">Index: {this.props.children}</div>
	}
}

class App extends React.Component {
	render(){
		return (
			<Provider store={store}>
				<Router history={reduxHistory}>
					<Route path="/" component={Index}>
						<Route path="/planner" component={Planner}/>
					</Route>
				</Router>
			</Provider>
		)
	}	
}

ReactDOM.render(<App/>, document.getElementById("app"))
