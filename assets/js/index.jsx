import React from "react"
import ReactDOM from "react-dom"

class App extends React.Component {
	render(){
		return <div>Hey this is react</div>
	}	
}

ReactDOM.render(<App/>, document.getElementById("app"))