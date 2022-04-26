#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
*check_cycle - function in C that checks if a
*singly linked list has a cycle in it.
*/
int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	while (1)
	{
		if (a->next != NULL && a->next->next != NULL)
		{
			a = a->next->next;
			b = b->next;
			if (a == b)
				return (1);
		}
		else
			return (0);
	}	 
}
