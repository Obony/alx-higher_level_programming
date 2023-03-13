#include "lists.h"
#include <stdio.h>

listint_t *reverse_listint(listint_t **head);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: beginning node of linked list
 *
 * Return: 0 if not a palindrome, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current, *new;

	current = *head;
	new = *head;
	reverse_listint(&new);

	while (current != NULL)
	{
		if (current->n != new->n)
		{
			return (0);
		}
		current = current->next;
		new = new->next;
	}
	return (1);
}

/**
 * reverse_listint - reverses a singly linked list
 * @head: pointer to beginning node
 *
 * Return: pointer to head of reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *temp, *prev = NULL;

	if ((*head) == NULL)
		return (NULL);
	if ((*head)->next == NULL)
		return (*head);
	while ((*head) != NULL)
	{
		temp = (*head)->next;
		(*head)->next = prev;
		prev = (*head);
		(*head) = temp;
	}
	*head = prev;
	return (*head);
}
