#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *temp, *current;
	int counter = 0, i;

	current = list;
	while(current)
	{
		temp = list;

		for(i = 0; i < counter; i++)
		{
			if (current == temp)
				return (1);
			temp = temp->next;
		}
		counter++;
		current = current->next;
	}
	return (0);
}
