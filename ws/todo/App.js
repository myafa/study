import * as React from 'react';
import { Text, View, StyleSheet, StatusBar, TextInput, Dimensions,Platform,ScrollView } from 'react-native';
import { Constants } from 'expo';
import ToDo from "./toDo"
const {height, width} = Dimensions.get("window")

export default class App extends React.Component {
  state = {
    newToDo: ""
  };
  render() {
    const{newToDo}= this.state;
    return (
      <View style={styles.container}>
        <StatusBar barStyle="light-content"/>
        <Text style ={styles.title}>To Do</Text>
        <View style={styles.card}>
         <TextInput 
          style={styles.input} 
          placeholder={"New"} 
          value={newToDo} 
          onChangeText={this._controlNewToDo}
          placeholderTextColor={"#999"}
          returnKeyType={"done"}
         />
  
      <ScrollView contentContainerStyle={styles.toDos}>
        <ToDo text={"Hell To Do"} />
      </ScrollView>
        </View>
      </View>
    );
  }
  _controlNewToDo = text=>{
    this.setState({
      newToDo: text
    })
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
 
    //paddingTop: Constants.statusBarHeight,
    backgroundColor: '#f23657',
  },
  title: {
    color: "white",
    fontSize: 30,
    marginTop: 50,
    marginBottom: 30,
    fontWeight: "200"
  },
  card:{
    backgroundColor: "white",
    flex: 1,
    width: width -25,
    borderTopLeftRadius: 10,
    borderTopRightRadius: 10,
    ...Platform.select({
      ios:{
        shadowColor:"rgb(50,50,50)",
        shadowOpacity: 0.5,
        shadowRadius: 5,
        shadowOffset: {
          height: -1,
          width: 0
        }
      },
      android: {
        elevation: 3
      }
    })
  },
  input: {
    padding: 20,
    borderBottomColor: "#bbb",
    borderBottomWidth: 1,
    fontSize: 25
  },
  toDos:{
    alignItems: "center"
  }
});
