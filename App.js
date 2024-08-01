import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';
import axios from 'axios';

const App = () => {
  const [legumes, setLegumes] = useState([]);
  const [fruits, setFruits] = useState([]);

  useEffect(() => {
    axios.get('http://192.168.68.68:5000/api/legumes')
      .then(response => setLegumes(response.data))
      .catch(error => console.error('Error fetching legumes:', error));

    axios.get('http://192.168.68.68:5000/api/fruits')
      .then(response => setFruits(response.data))
      .catch(error => console.error('Error fetching fruits:', error));
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
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 40,
    paddingHorizontal: 20
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20
  },
  item: {
    fontSize: 18,
    marginBottom: 10
  }
});

export default App;
