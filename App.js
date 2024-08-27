import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';
import axios from 'axios';

const App = () => {
  const [legumes, setLegumes] = useState([]);
  const [fruits, setFruits] = useState([]);
  const [users, setUsers] = useState([]);
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('http://10.0.2.2:5000/api/legumes')
      .then(response => setLegumes(response.data))
      .catch(error => console.error('Error fetching legumes:', error)) ;

    axios.get('http://10.0.2.2:5000/api/fruits')
      .then(response => setFruits(response.data))
      .catch(error => console.error('Error fetching fruits:', error));

    axios.get('http://10.0.2.2:5000/users')
    .then(response => setUsers(response.data))
    .catch(error => console.error('Error fetching users:', error));
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Liste des Légumes</Text>
      <FlatList
        data={legumes}
        keyExtractor={item => item.id.toString()}
        renderItem={({ item }) => <Text style={styles.item}>{item.name}</Text>}
      />

      <Text style={styles.title}>Liste des Fruits</Text>
      <FlatList
        data={fruits}
        keyExtractor={item => item.id.toString()}
        renderItem={({ item }) => <Text style={styles.item}>{item.name}</Text>}
      />
      <Text style={styles.title}>Liste des Users</Text>
      <FlatList
        data={users}
        // keyExtractor={item => item.id.toString()}
        renderItem={({ item }) => <Text style={styles.item}>{item.email}</Text>}
      />
      <Text style={styles.container}>{data ? data : "Loading..."}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 40,
    paddingHorizontal: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  item: {
    fontSize: 18,
    marginBottom: 10,
  },
});

export default App;
