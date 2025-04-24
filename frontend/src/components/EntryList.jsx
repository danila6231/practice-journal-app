import React, { useState, useEffect } from 'react';
import { 
  Box, 
  Paper, 
  Typography, 
  Chip,
  Divider,
  CircularProgress
} from '@mui/material';
import { format } from 'date-fns';
import axios from 'axios';

const EntryList = () => {
  const [entries, setEntries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchEntries = async () => {
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_URL}/api/entries`);
        setEntries(response.data);
      } catch (err) {
        setError('Failed to load entries. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchEntries();
  }, []);

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" p={3}>
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return (
      <Typography color="error" align="center" p={3}>
        {error}
      </Typography>
    );
  }

  return (
    <Box>
      <Typography variant="h5" gutterBottom>
        Your Journal Entries
      </Typography>
      {entries.map((entry, index) => (
        <Paper key={entry._id} elevation={2} sx={{ p: 3, mb: 3 }}>
          <Box display="flex" justifyContent="space-between" alignItems="center" mb={2}>
            <Typography variant="subtitle2" color="textSecondary">
              {format(new Date(entry.created_at), 'MMMM d, yyyy')}
            </Typography>
            <Chip 
              label={entry.mood_tag} 
              color="primary" 
              variant="outlined"
            />
          </Box>
          <Typography variant="body1" paragraph>
            {entry.content}
          </Typography>
          <Divider sx={{ my: 2 }} />
          <Typography variant="subtitle2" color="textSecondary">
            AI Summary:
          </Typography>
          <Typography variant="body2">
            {entry.summary}
          </Typography>
        </Paper>
      ))}
    </Box>
  );
};

export default EntryList; 