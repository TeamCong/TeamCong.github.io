import { render, screen } from '@testing-library/react';
import App from './App';

test('renders portfolio container', () => {
  render(<App />);
  const portfolioElement = screen.getByText(/iOS Developer & App Creator/i);
  expect(portfolioElement).toBeInTheDocument();
});
