import React, {Component} from "react";
import { View,Text,TouchableOpacity,StyleSheet,Dimensions} from "react-native";

const {width, height} =Dimensions.get("window");

export default class ToDo extends Component{
  state = {
    isEditing: false,
    isCompleted: false,
    toDoValue: ""
  };
  render(){
    const {isCompleted, isEditing} = this.state;
    const { text} = this.props;
    return(
      <View style={styles.container}>
        <View style={styles.column}>
          <TouchableOpacity onPress={this._toggleComplete}>
            <View style={[styles.circle,
                  isCompleted ? styles.completedCircle : styles.incompleteCircle 
                  ]} />
          </TouchableOpacity>
          <Text style={[styles.text, isCompleted ? styles.completedText: styles.incompleteText]}>abra</Text>
        </View>
        <View style={styles.column}>
          {isEditing ? 
            <View style={styles.actions}>
              <TouchableOpacity onPressOut={this._finishEditing}>
                <View style={styles.actionContainer}>
                  <Text style={styles.actionText}></Text>
                </View>
              </TouchableOpacity>
            </View> : <View style={styles.actions}>
              <TouchableOpacity onPressOut={this._startEditing}>
                <View style={styles.actionContainer}>
                  <Text style={styles.actionText}></Text>
                </View>
              </TouchableOpacity>
              <TouchableOpacity>
                <View style={styles.actionContainer}>
                  <Text style={styles.actionText}></Text>
                </View>
              </TouchableOpacity>
            </View>
          }
        </View>
      </View>
    )
  }

  _toggleComplete=()=>{
    this.setState(prevState=>{
      return({
        isCompleted: !prevState.isCompleted
      });
    });
  };
  _startEditing=()=>{
    this.setState({
      isEditing: true
      });
  };
  _finishEditing =()=>{
    this.setState({
      isEditing: false
    });
  };
}
const styles = StyleSheet.create({
  container: {
    width: width-50,
    borderBottomColor:"#bbb",
    borderBottomWidth: StyleSheet.hairlineWidth,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems:"center"
  },
  text:{
    fontWeight: "600",
    fontSize: 20,
    marginVertical:20
  },
  circle:{
    width:30,
    height: 30,
    borderRadius: 15,
    borderColor: "red",
    borderWidth: 3,
    marginRight: 20,
   // backgroundColor: "red"
  },
  completedCircle:{
    borderColor: "#bbb"
  },
    incompleteCircle:{
    borderColor: "#F23657"
  },
  completedText:{
    color:"#bbb",
    textDecorationLine: "line-through"
  },
  incompleteText: {
    color: "#353535"
  },
  column: {
    flexDirection: "row",
    alignItems: "center",
    width:width/2,
    justifyContent: "space-between"
  },
  actions: {
    flexDirection: "row"
  },
  actionContainer: {
    marginVertical: 10,
    marginHorizontal: 10
  }
})