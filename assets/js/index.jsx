import React from "react"
import ReactDOM from "react-dom"
import { Router, Route, browserHistory } from "react-router"
import { Provider } from "react-redux"
import { syncHistoryWithStore } from "react-router-redux"
import { createStore } from "redux"

reducer = function(state){
	return state
}

store = createStore(reducer)
reduxHistory = syncHistoryWithStore(browserHistory, store)

class Index extends React.Component{

	render(){
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