import React, {Component} from "react"
import {Row, Col} from "react-bootstrap"

const tripData = [
	{id: 1, number: 75},
	{id: 2, number: 100},
	{id: 3, number: 1000}
]

class Trip extends Component{
	render(){
		return <Col xs={4} className="text-center">{this.props.trip.number}</Col>
	}
}
export default class Planner extends Component{
	render(){
		return(
			<Row id="planner">
				{
					tripData.map(
						trip => <Trip trip={trip} key={trip.id}/>
					)
				}
			</Row>
		)
	}
}