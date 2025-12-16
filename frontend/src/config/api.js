/**
 * Centralized API configuration
 * 
 * This module provides the base API URL that adapts to the environment:
 * - Development (Vite on port 5173): Uses localhost:8000 (separate backend server)
 * - Production/Docker (served on port 8000): Uses relative URLs (same origin)
 */

// Detect environment based on port
// Vite dev server runs on port 5173, so if we're on 5173, we're in development
const isDevelopment = window.location.port === '5173';
const API_BASE_URL = isDevelopment ? 'http://localhost:8000' : '';

/**
 * Get the full API URL for a given endpoint
 * @param {string} endpoint - API endpoint path (e.g., '/api/layer_hierarchy')
 * @returns {string} Full API URL
 */
export const getApiUrl = (endpoint) => {
  // Ensure endpoint starts with /
  const path = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  return `${API_BASE_URL}${path}`;
};

/**
 * Fetch wrapper with automatic API URL resolution
 * @param {string} endpoint - API endpoint path
 * @param {RequestInit} options - Fetch options
 * @returns {Promise<Response>} Fetch response
 */
export const apiFetch = async (endpoint, options = {}) => {
  const url = getApiUrl(endpoint);
  return fetch(url, options);
};

// Export the base URL for direct access if needed
export { API_BASE_URL };

export default {
  getApiUrl,
  apiFetch,
  API_BASE_URL,
};
