import React from 'react';
import { Container, CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import JournalForm from './components/JournalForm';
import EntryList from './components/EntryList';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    background: {
      default: '#f5f5f5',
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="md" sx={{ py: 4 }}>
        <JournalForm />
        <EntryList />
      </Container>
    </ThemeProvider>
  );
}

export default App; 