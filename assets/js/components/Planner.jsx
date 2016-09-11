import React, {Component} from "react"
import {Row, Col, ListGroup, ListGroupItem} from "react-bootstrap"

const tripData = [
	{id: 1, number: 75, foppers: ["Derp", "Herp", "Yo"]},
	{id: 2, number: 100, foppers: ["Derp", "Herp", "Yo"]},
	{id: 3, number: 1000, foppers: ["Derp", "Herp", "Yo"]}
]

class Trip extends Component{
	render(){
		return(
			<Col xs={4}>
				<ListGroup>
					{this.props.trip.number}
					{this.props.trip.foppers.map((fopper, i) => <ListGroupItem key={i}>{fopper}</ListGroupItem>)}
				</ListGroup>
			</Col>)
	}
}
export default class Planner extends Component{
	render(){
		return(
			<Row id="planner">
				{tripData.map(trip => <Trip trip={trip} key={trip.id}/>)}
			</Row>
		)
	}
}